
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

pipe = pipeline(Tasks.text_to_video, model='damo-vilab/text-to-video-ms-1.7b')
video = pipe("cinematic slow motion")
video['output_video'].save("output/modelscope.mp4")
