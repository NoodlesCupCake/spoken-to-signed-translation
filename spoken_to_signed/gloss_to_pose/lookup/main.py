from pose_format import Pose
from pose_format.pose_visualizer import PoseVisualizer
from spoken_to_signed.gloss_to_pose import concatenate_poses
with open("assets\dummy_lexicon\sgg\กระเพาะอาหาร.pose", "rb") as f:
    
    pose1 = Pose.read(f.read())
with open("assets\dummy_lexicon\sgg\กระบือ.pose", "rb") as f:
    pose2 = Pose.read(f.read())

poses = [pose1, pose2]
p = concatenate_poses(poses)

# Resize to 256, for visualization speed
scale = p.header.dimensions.width / 256
p.header.dimensions.width = int(p.header.dimensions.width / scale)
p.header.dimensions.height = int(p.header.dimensions.height / scale)
p.body.data = p.body.data / scale

# Genearate .gif
v = PoseVisualizer(p)
v.save_gif("กระเพาะอาหารกระบือ.gif", v.draw())