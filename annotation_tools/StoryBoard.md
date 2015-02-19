# StoryBoard

## Annotation des preuves OCR

#### Informations en entrées : 
 - nom de la personne
 - nom de la vidéo 
 - timestamp où le nom est écrit à l'écran
 - timestamp où apparait la personne (identique au précédent ???)
 
#### Scénario :
 - On affiche le nom de la personne correspondant à la preuve.
 - On affiche la vidéo où le nom est écrit à l'écran, calée sur le timestamp fourni.
 - On affiche la vidéo où apparait la personne, calée sur le timestamp fourni.
 - On demande à l'utilisateur de cliquer sur le visage correspondant au nom.
 - Si l'annotateur ne voit pas la personne correspondante dans l'image affichée, elle peut lire le plan de la vidéo pour trouver une meilleur image.
 - Si elle ne trouve pas la personne, elle clique sur un bouton.
 - Correction du nom de la personne ???

![OCR](OCR.png)


## Annotation des preuves ASR

#### Informations en entrées : 
 - nom de la personne
 - nom de la vidéo 
 - timestamp où le nom est prononcé
 - timestamp où apparait la personne (proche du précédent ???)
 - La phrase prononcée et le nom taggé

#### Scénario :
 - On affiche le nom de la personne correspondant à la preuve.
 - On affiche le segment vidéo où le nom est prononcé, calée sur le timestamp fourni -10 secondes.
 - On affiche la segment vidéo où apparait la personne, calée sur le timestamp fourni.
 - On joue la vidéo pendant 20 secondes pour vérifier si le bon nom a été prononcé
 - On demande à l'utilisateur de cliquer sur le visage correspondant au nom.
 - Si l'annotateur ne voit pas la personne correspondante dans l'image affiché, elle peut lire le plan de la vidéo pour trouver une meilleur image.
 - Si elle ne trouve pas la personne, elle clique sur un bouton.
 - Correction du nom de la personne ???
 
 ![ASR](ASR.png)

 
## Vérification de l'identité des visages

- On affiche l'image d'une preuve + un nom.
- On affiche une liste d'imagettes correspondant au centre de chacun des plans à annoter pour une vidéo.
- Si la personne correspondante est visible, l'annotateur clique sur son visage.
- Si la personne n'est pas visible, l'annotateur peut chercher une meilleur image dans le plan en lisant la vidéo.
- Si la personne n'apparait pas dans le plan, elle clique sur un bouton.

 ![Face](Face.png)

## Vérification si les visages parlent

- On affiche un plan avec un visage entouré (celui sur lequel l'annotateur a cliqué dans l'étape précédente).
- L'annotateur joue la vidéo est vérifie si la personne parle dans le plan.

On peut utiliser un classifieur pour savoir si le visage parle ou non, et l'on annote manuellement que les cas négatifs ou limites

 ![Speaking_face](Speaking_face.png)
