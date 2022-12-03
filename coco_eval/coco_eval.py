"""python -u coco_eval/coco_eval.py --trg coco_caps/trans_scl_test.json
"""

import argparse
import os
from pycocotools.coco import COCO
from pycocoevalcap.eval import COCOEvalCap


parser = argparse.ArgumentParser()
parser.add_argument('--anno', type=str, default='coco_eval/captions_val2014.json')
parser.add_argument('--trg', type=str, default='coco_caps/sample_captions.json')
args = parser.parse_args()


# create coco object and coco_result object
coco = COCO(args.anno)
coco_result = coco.loadRes(args.trg)

# create coco_eval object by taking coco and coco_result
coco_eval = COCOEvalCap(coco, coco_result)

# evaluate on a subset of images by setting
# coco_eval.params['image_id'] = coco_result.getImgIds()
# please remove this line when evaluating the full validation set
coco_eval.params['image_id'] = coco_result.getImgIds()

# evaluate results
# SPICE will take a few minutes the first time, but speeds up due to caching
coco_eval.evaluate()

# print output evaluation scores
for metric, score in coco_eval.eval.items():
    print(f'{metric}: {score:.3f}')


print("Done")
