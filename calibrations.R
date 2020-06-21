library(lme4)

df = read.csv('/Users/JonahKrop/Documents/Projects/Baseball/test_df.csv')

model = lmer('release_pos_x ~ 1 + (factor(year)|home_team)', data=df[!is.na(df$release_speed),])
ranef(model)