# merge the data frames together!
# this will be redone after data is properly cleaned!
import pandas as pd
root = "pickles/"
train_df = pd.read_pickle(root + "train_df.pkl")
test_df = pd.read_pickle(root + "test_df.pkl")
weather_train_df = pd.read_pickle(root + "weather_train_df.pkl")
weather_test_df = pd.read_pickle(root + "weather_test_df.pkl")
building_meta_df = pd.read_pickle(root + "building_meta_df.pkl")
train_df['timestamp'] = pd.to_datetime(train_df['timestamp'])
test_df['timestamp'] = pd.to_datetime(test_df['timestamp'])
weather_train_df['timestamp'] = pd.to_datetime(weather_train_df['timestamp'])
weather_test_df['timestamp'] = pd.to_datetime(weather_test_df['timestamp'])
building_meta_df['primary_use'] = building_meta_df['primary_use'].astype('category')
temp_df = train_df[['building_id']]
temp_df = temp_df.merge(building_meta_df, on=['building_id'], how='left')
del temp_df['building_id']
train_df = pd.concat([train_df, temp_df], axis=1)
temp_df = test_df[['building_id']]
temp_df = temp_df.merge(building_meta_df, on=['building_id'], how='left')
del temp_df['building_id']
test_df = pd.concat([test_df, temp_df], axis=1)
del temp_df, building_meta_df
temp_df = train_df[['site_id','timestamp']]
temp_df = temp_df.merge(weather_train_df, on=['site_id','timestamp'], how='left')
del temp_df['site_id'], temp_df['timestamp']
train_df = pd.concat([train_df, temp_df], axis=1)
temp_df = test_df[['site_id','timestamp']]
temp_df = temp_df.merge(weather_test_df, on=['site_id','timestamp'], how='left')
del temp_df['site_id'], temp_df['timestamp']
test_df = pd.concat([test_df, temp_df], axis=1)
del temp_df, weather_train_df, weather_test_df
train_df.to_pickle("pickles/train_merged.pkl")
test_df.to_pickle("pickles/test_merged.pkl")



