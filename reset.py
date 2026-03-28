from pathlib import Path

from blind_watermark import WaterMark

input_dir = Path("input")
output_dir = Path("output")
input_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)


def reset_watermark(input, output):
    bwm1 = WaterMark(password_img=3545, password_wm=4521)
    bwm1.read_img(input)

    bwm1.bwm_core.init_block_index()
    block_num = bwm1.bwm_core.block_num
    wm = [True] * (int(block_num) - 1)

    bwm1.read_wm(wm, mode="bit")
    bwm1.embed(output)
    len_wm = len(bwm1.wm_bit)
    print(f"{block_num=} Put down the length of wm_bit {len_wm}")


for i in input_dir.iterdir():
    if i.suffix not in [".jpg", ".png", ".jpeg"]:
        continue

    reset_watermark(i, output_dir / i.name)
