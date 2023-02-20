import pandas as pd


#  國際盤
A, B, C = 1, 1, 1

df_int = pd.DataFrame(columns=['國際盤', '目前累計戰績', '莊家殺手標準', '達到標準'])
df_int.loc[0] = ['本賽季總勝率', A, B, C]
df_int.loc[1] = ['雙周最低注數', A, B, C]
df_int.loc[2] = ['第一周最低注數', A, B, C]
df_int.loc[3] = ['第二周最低注數', A, B, C]
df_int.loc[4] = ['雙周總勝率', A, B, C]
df_int.loc[5] = ['雙周總獲利', A, B, C]
df_int.loc[6] = ['總計注數', A, B, C]


#  運彩盤
A, B, C = 1, 1, 1

df_civ = pd.DataFrame(columns=['運彩盤', '目前累計戰績', '莊家殺手標準', '達到標準'])
df_civ.loc[0] = ['本賽季總勝率', A, B, C]
df_civ.loc[1] = ['雙周最低注數', A, B, C]
df_civ.loc[2] = ['第一周最低注數', A, B, C]
df_civ.loc[3] = ['第二周最低注數', A, B, C]
df_civ.loc[4] = ['雙周總勝率', A, B, C]
df_civ.loc[5] = ['雙周總獲利', A, B, C]
df_civ.loc[6] = ['總計注數', A, B, C]
