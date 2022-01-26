import matplotlib.pyplot as plt
# import seaborn as sns; sns.set()
import pandas as pd


df = pd.DataFrame({
    'x': [],
    'y': [],
    'z': []
})

# from sklearn.datasets.samples_generator import make_blobs
# X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# plt.scatter(df['x'], df['y'], s=50);

# from sklearn.cluster import KMeans

# kmeans = KMeans(n_clusters=4)
# kmeans.fit(df)


# labels = kmeans.predict(df)
# print(labels)

# # plt.scatter(df['x'], df['y'], c=labels, s=50, cmap='viridis')

# centers = kmeans.cluster_centers_
# print(centers)
# plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
# plt.show()
# df['x'].append(5)
for i in range(10):
    df = df.append({'x' : 0}, ignore_index=True)

print(df['x'])

# data = [['Ali','Azmat','30'],['Sharukh','Khan','40'],['Linus','Torvalds','70']]
# df = pd.DataFrame(data,) 
# print(data['First'])



'''k-means'''
                # print(storage_face)
                # for i in range(body_test_size):
                #     df_amu = df_amu.append({'amu': storage_face[i][0]}, ignore_index=True)
                #     df_pri = df_pri.append({'pri': storage_face[i][1]}, ignore_index=True)
                #     df_joy = df_joy.append({'joy': storage_face[i][2]}, ignore_index=True)
                #     df_fea = df_fea.append({'fea': storage_face[i][3]}, ignore_index=True)
                #     df_anx = df_anx.append({'anx': storage_face[i][4]}, ignore_index=True)
                #     df_des = df_des.append({'des': storage_face[i][5]}, ignore_index=True)
                #     df_sad = df_sad.append({'sad': storage_face[i][6]}, ignore_index=True)
                #     df_ang = df_ang.append({'ang': storage_face[i][7]}, ignore_index=True)
                #     df_irr = df_irr.append({'irr': storage_face[i][8]}, ignore_index=True)
                #     df_int = df_int.append({'int': storage_face[i][9]}, ignore_index=True)
                #     df_ple = df_ple.append({'ple': storage_face[i][10]}, ignore_index=True)
                #     df_rel = df_rel.append({'rel': storage_face[i][11]}, ignore_index=True)

                #     df_amu = df_amu.append({'amu': storage_body[i][0]}, ignore_index=True)
                #     df_pri = df_pri.append({'pri': storage_body[i][1]}, ignore_index=True)
                #     df_joy = df_joy.append({'joy': storage_body[i][2]}, ignore_index=True)
                #     df_fea = df_fea.append({'fea': storage_body[i][3]}, ignore_index=True)
                #     df_anx = df_anx.append({'anx': storage_body[i][4]}, ignore_index=True)
                #     df_des = df_des.append({'des': storage_body[i][5]}, ignore_index=True)
                #     df_sad = df_sad.append({'sad': storage_body[i][6]}, ignore_index=True)
                #     df_ang = df_ang.append({'ang': storage_body[i][7]}, ignore_index=True)
                #     df_irr = df_irr.append({'irr': storage_body[i][8]}, ignore_index=True)
                #     df_int = df_int.append({'int': storage_body[i][9]}, ignore_index=True)
                #     df_ple = df_ple.append({'ple': storage_body[i][10]}, ignore_index=True)
                #     df_rel = df_rel.append({'rel': storage_body[i][11]}, ignore_index=True)
                    # df_face = df_face.append({
                    #     'amu': storage_face[i][0],
                    #     'pri': storage_face[i][1],
                    #     'joy': storage_face[i][2],
                    #     'fea': storage_face[i][3],
                    #     'anx': storage_face[i][4],
                    #     'des': storage_face[i][5],
                    #     'sad': storage_face[i][6],
                    #     'ang': storage_face[i][7],
                    #     'irr': storage_face[i][8],
                    #     'int': storage_face[i][9],
                    #     'ple': storage_face[i][10],
                    #     'rel': storage_face[i][11]
                    # }, ignore_index=True)
                    # df_face = df_face.append({
                    #     'amu': storage_body[i][0],
                    #     'pri': storage_body[i][1],
                    #     'joy': storage_body[i][2],
                    #     'fea': storage_body[i][3],
                    #     'anx': storage_body[i][4],
                    #     'des': storage_body[i][5],
                    #     'sad': storage_body[i][6],
                    #     'ang': storage_body[i][7],
                    #     'irr': storage_body[i][8],
                    #     'int': storage_body[i][9],
                    #     'ple': storage_body[i][10],
                    #     'rel': storage_body[i][11]
                    # }, ignore_index=True)

                # print(df_face['amu'])

                # kmeans.fit(df_amu)
                # centers.append(kmeans.cluster_centers_)

                # storage_face_mx = storage_face * centers

                # kmeans.fit(df_body)
                # centers = kmeans.cluster_centers_
                # print(centers)
                # centers = ones_matrix - centers
                # storage_body_mx = storage_body * centers


    # df_face = pd.DataFrame({
    #         'amu': [],
    #         'pri': [],
    #         'joy': [],
    #         'fea': [],
    #         'anx': [],
    #         'des': [],
    #         'sad': [],
    #         'ang': [],
    #         'irr': [],
    #         'int': [],
    #         'ple': [],
    #         'rel': []
    #     })
    
    # df_body = pd.DataFrame({
    #     'amu': [],
    #     'pri': [],
    #     'joy': [],
    #     'fea': [],
    #     'anx': [],
    #     'des': [],
    #     'sad': [],
    #     'ang': [],
    #     'irr': [],
    #     'int': [],
    #     'ple': [],
    #     'rel': []
    # })

    # df_amu = pd.DataFrame({'amu': []})
    # df_pri = pd.DataFrame({'pri': []})
    # df_joy = pd.DataFrame({'joy': []})
    # df_fea = pd.DataFrame({'fea': []})
    # df_anx = pd.DataFrame({'anx': []})
    # df_des = pd.DataFrame({'des': []})
    # df_sad = pd.DataFrame({'sad': []})
    # df_ang = pd.DataFrame({'ang': []})
    # df_irr = pd.DataFrame({'irr': []})
    # df_int = pd.DataFrame({'int': []})
    # df_ple = pd.DataFrame({'ple': []})
    # df_rel = pd.DataFrame({'rel': []})