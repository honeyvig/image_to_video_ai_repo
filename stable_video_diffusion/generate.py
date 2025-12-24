
from diffusers import StableVideoDiffusionPipeline
from PIL import Image
import torch

pipe = StableVideoDiffusionPipeline.from_pretrained(
    "stabilityai/stable-video-diffusion-img2vid",
    torch_dtype=torch.float16
).to("cuda")

image = Image.open("../images/input.jpg")
frames = pipe(image=image, num_frames=25).frames
pipe.export_to_video(frames, "../output/svd.mp4", fps=6)
