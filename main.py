import cv2
import numpy as np

# création du tableau
image = cv2.imread("img.jpg", cv2.IMREAD_COLOR)
colonnes = np.array(image)

# Logique

for i in range(51, len(colonnes), 100):
    for j in range(51, len(colonnes[i]), 100):
        values = np.random.randint(0, 256, 3)
        for k in range(-101, 102):
            for l in range(-101, 102):
                if 0 <= i + k < len(colonnes) and 0 <= j + l < len(colonnes[i + k]):
                    if (
                        colonnes[i + k][j + l][2] > 100
                        and colonnes[i + k][j + l][1] < 110
                        and colonnes[i + k][j + l][0] < 150
                    ):
                        colonnes[i + k][j + l] = values
    print(str(i) + "/" + str(len(colonnes)))


# sauvegarde de l'image
image_finale = np.array(colonnes)
cv2.imwrite("img_changed.jpg", image_finale)
