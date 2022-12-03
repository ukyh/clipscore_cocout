import argparse
import os
import json


parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='eval_results_oscar/target_captions.json')
parser.add_argument('--out_dir', type=str, default='coco_caps_oscar')
args = parser.parse_args()

N = 5000


cap_list = []
with open(args.input) as f:
    d = json.load(f)
    cap_list = [{"image_id": int(item['image_id']), "caption": item['caption']} for item in d]
    assert len(cap_list) == N

outfile = os.path.join(args.out_dir, os.path.split(args.input)[-1])
with open(outfile, "w") as outf:
    json.dump(cap_list, outf, indent=4)


print("Done")
