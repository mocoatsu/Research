# 遺伝子型の最小値、最大値を保持
# 報知のイメージが強い音の群 での，立ち上がり時間の平均は143ms
ATTACK_RANGE = (0, 0.25)
DECAY_RANGE = (0, 0.25)
SUSTAIN_RANGE = (0, 1)
SUSTAIN_TIME_RANGE = (0, 0.25)
# 4kHzでは0〜100msがチッ、100〜200msがチン、300ms以上がチーン
RELEASE_RANGE = (0, 0.35)
FREQUENCY_RANGE = (300, 1200)
RATIO_TO_CARRIER_FREQUENCY_RANGE = (1, 4)
MODULATION_INDEX_RANGE = (0, 300)
ALGORITHM_NUM : str = 1

GENERATION_CHROMOSOME_NUM:int = 10
NUM_PARAM = 8