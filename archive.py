# rouge -> rand
# création du tableau
# image = cv2.imread("img.jpg", cv2.IMREAD_COLOR)
# colonnes = [image[:, i] for i in range(image.shape[1])]
# colonnesV2 = np.array(colonnes)

# # Logique

# for i in range(len(colonnesV2)):
#     # num = np.random.randint(0, 5)
#     for j in range(len(colonnesV2[i])):
#         if (
#             colonnesV2[i][j][2] > 100
#             and colonnesV2[i][j][1] < 110
#             and colonnesV2[i][j][0] < 150
#         ):
#             colonnesV2[i][j] = [np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)]

#     print(str(i) + "/" + str(len(colonnesV2)))


# # sauvegarde de l'image
# image_finale = [colonnesV2[:, i] for i in range(len(colonnesV2[0]))]
# image_finaleV2 = np.array(image_finale)
# cv2.imwrite("img_changed.jpg", image_finaleV2)
