import numpy as np
import tensorflow as tf


seed: int = 13371337

np.random.seed(seed)
tf.set_random_seed(seed)


class ImageDataLoader:
    def __init__(self,
                 patch_shape: tuple = (128, 128),
                 channels: int = 3,
                 patch_size: int = 16):
        self.patch_shape = patch_shape
        self.channels = channels
        self.patch_size = patch_size
        self.scale = int(np.sqrt(self.patch_size))

        self.lr_patch_shape = (
            self.patch_shape[0],
            self.patch_shape[1])
        self.hr_patch_shape = (
            self.patch_shape[0] * self.scale,
            self.patch_shape[1] * self.scale
        )

    def random_crop(self, x_lr, x_hr):
        x_hr_shape = x_hr.get_shape().as_list()

        rand_lr_w = (np.random.randint(0, x_hr_shape[0] - self.hr_patch_shape[0])
                     // self.scale)
        rand_lr_h = (np.random.randint(0, x_hr_shape[1] - self.hr_patch_shape[1])
                     // self.scale)
        rand_hr_w = rand_lr_w * self.scale
        rand_hr_h = rand_lr_h * self.scale

        x_lr = x_lr[rand_lr_w:rand_lr_w + self.lr_patch_shape[0], rand_lr_h:rand_lr_h + self.lr_patch_shape[1], :]
        x_hr = x_hr[rand_hr_w:rand_hr_w + self.hr_patch_shape[0], rand_hr_h:rand_hr_h + self.hr_patch_shape[1], :]
        return x_lr, x_hr

    def pre_processing(self, fn):
        lr = tf.read_file(fn[0])
        lr = tf.image.decode_png(lr, channels=self.channels)
        lr = tf.cast(lr, dtype=tf.float32) / 255.

        hr = tf.read_file(fn[1])
        hr = tf.image.decode_png(hr, channels=self.channels)
        hr = tf.cast(hr, dtype=tf.float32) / 255.

        # random crop
        lr, hr = self.random_crop(lr, hr)

        # augmentations
        if np.random.randint(0, 2) == 0:
            lr = tf.image.flip_up_down(lr)
            hr = tf.image.flip_up_down(hr)

        if np.random.randint(0, 2) == 0:
            lr = tf.image.rot90(lr)
            hr = tf.image.rot90(hr)

        # split into patches
        lr_patches = tf.image.extract_image_patches(
            images=tf.expand_dims(lr, axis=0),
            ksizes=(1,) + self.lr_patch_shape + (1,),
            strides=(1,) + self.lr_patch_shape + (1,),
            rates=[1, 1, 1, 1],
            padding='VALID'
        )
        lr_patches = tf.reshape(lr_patches,
                                (-1,) + self.lr_patch_shape + (self.channels,))

        hr_patches = tf.image.extract_image_patches(
            images=tf.expand_dims(hr, axis=0),
            ksizes=(1,) + self.hr_patch_shape + (1,),
            strides=(1,) + self.hr_patch_shape + (1,),
            rates=[1, 1, 1, 1],
            padding='VALID'
        )
        hr_patches = tf.reshape(hr_patches,
                                (-1,) + self.hr_patch_shape + (self.channels,))

        return lr_patches, hr_patches
