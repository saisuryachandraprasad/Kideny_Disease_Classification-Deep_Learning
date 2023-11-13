import os
import tensorflow as tf
from pathlib import Path
from src.Kidney_Disease_Classifier.config.configuration import TrainingConfig




class Training:
    def __init__(self, config = TrainingConfig):
        self.config = config

    def get_base_model(self):
        """ This method responsible to load model from updated model from base model pipeline"""
        self.model = tf.keras.models.load_model(
            self.config.updated_model_path
        )

    
    def train_valid_generator(self):

        data_generator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.2
            )
        
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            interpolation = "bilinear",
            batch_size =self.config.params_batch_size

        )
        
        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        self.valid_generator = valid_data_generator.flow_from_directory(
            directory=self.config.training_data,
            subset= "validation",
            shuffle=False,
            **dataflow_kwargs,
        )

        if self.config.params_is_augamentation:
            training_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **data_generator_kwargs
            )

        else:
            training_datagenerator = valid_data_generator

        self.train_generator = training_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset='training',
            shuffle= False,
            **dataflow_kwargs
        )
    @staticmethod
    def save_model(path : Path, model:tf.keras.Model):
        model.save(path)

    def train(self):
        self.step_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size


        self.model.fit(
            self.train_generator,
            epochs = self.config.params_epoch,
            steps_per_epoch = self.step_per_epoch,
            validation_steps = self.validation_steps,
            validation_data = self.valid_generator
        )

        self.save_model(
            path= self.config.trained_model_path,
            model = self.model
        )