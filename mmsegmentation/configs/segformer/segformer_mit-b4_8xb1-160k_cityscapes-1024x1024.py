_base_ = ["./segformer_mit-b0_8xb1-160k_cityscapes-1024x1024.py"]

model = dict(
    backbone=dict(
        init_cfg=dict(type="Pretrained", checkpoint="pretrain/mit_b4.pth"),
        embed_dims=64,
        num_layers=[3, 8, 27, 3],
    ),
    decode_head=dict(in_channels=[64, 128, 320, 512]),
)