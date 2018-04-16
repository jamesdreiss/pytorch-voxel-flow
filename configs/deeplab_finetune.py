# DeepLab model
model = dict(
    name="DeepLab",
    backbone=dict(
        type='sense_resnet101',
        bn_param=dict(momentum=0.9997),
        bn_training=False,
        bn_parallel=False,
        layers_stride=[1, 2, 1, 1],
        layers_dilation=[1, 1, 2, [i * 4 for i in [1, 2, 4]]],
        mult_conv_w=[1, 1],  # lr, decay
        mult_conv_b=[2, 0],  # lr, decay
        mult_bn=[1, 1],  # lr, decay
    ),
    aspp=dict(
        channels=256,
        kernel_size=3,
        dilation_series=[6, 12, 18],
        image_pooling=True,
        bn_param=dict(momentum=0.9997),
        bn_training=False,
        bn_parallel=False,
        mult_conv_w=[1, 1],  # lr, decay
        mult_conv_b=[2, 0],  # lr, decay
        mult_bn=[1, 1],  # lr, decay
    ),
    classifier=dict(
        bn_param=dict(momentum=0.9997),
        bn_training=False,
        bn_parallel=False,
        num_class=21,
        dropout=0.1,
        mult_conv_w=[1, 1],  # lr, decay
        mult_conv_b=[2, 0],  # lr, decay
        mult_bn=[1, 1],  # lr, decay
    ))

device = [0, 1, 2, 3, 4, 5, 6, 7]
resume = 'outputs/deeplab_pretrain_checkpoint.pth.tar'
weight = ''
dataset = 'VOC2012'

# Training strategry
train = dict(
    batch_size=16,
    optimizer=dict(
        algorithm='SGD',
        args=dict(
            base_lr=0.0001,
            momentum=0.9,
            weight_decay=0.00004,
            policy='poly',
            learning_power=0.9,
            # policy='step',
            # rate_decay_factor=0.1,
            # rate_decay_step=2000,
            max_epoch=55)),
    data_list='train_val',
    crop_size=[513, 513],
    rotation=[-10, 10],
    blur=True,
    crop_policy='random',
    flip=True,
    scale_factor=[0.5, 2.0])

# Testing strategry
test = dict(
    batch_size=16,
    data_list='val',
    crop_size=[513, 513],
    crop_policy='center',
    scale_factor=[1.0])

# Logging
output_dir = 'outputs'
snapshot_pref = 'deeplab'
logging = dict(log_dir='', print_freq=50, eval_freq=10)
