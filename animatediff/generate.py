
from diffusers import AnimateDiffPipeline
import torch

pipe = AnimateDiffPipeline.from_pretrained(
    "guoyww/animatediff-motion-adapter-v1-5",
    torch_dtype=torch.float16
).to("cuda")

result = pipe(prompt="cinematic motion", num_frames=24)
result.export("output/animatediff.mp4")
