# CNN

## Content
The data is images and labels / annotations for mammography scans. More about the database can be found at MIAS. The 'Preview' kernel shows how the Info.txt and PGM files can be parsed correctly.

## Labels
1st column:
MIAS database reference number.

2nd column:
Character of background tissue:
F Fatty
G Fatty-glandular
D Dense-glandular

3rd column:
Class of abnormality present:
CALC Calcification
CIRC Well-defined/circumscribed masses
SPIC Spiculated masses
MISC Other, ill-defined masses
ARCH Architectural distortion
ASYM Asymmetry
NORM Normal

4th column:
Severity of abnormality;
B Benign
M Malignant

5th, 6th columns:
x,y image-coordinates of centre of abnormality.

7th column:
Approximate radius (in pixels) of a circle enclosing the abnormality.
There are also several things you should note:
The list is arranged in pairs of films, where each pair represents the left (even filename numbers) and right mammograms (odd filename numbers) of a single patient.
The size of all the images is 1024 pixels x 1024 pixels. The images have been centered in the matrix.
When calcifications are present, centre locations and radii apply to clusters rather than individual calcifications. Coordinate system origin is the bottom-left corner.
In some cases calcifications are widely distributed throughout the image rather than concentrated at a single site. In these cases centre locations and radii are inappropriate and have been omitted.

## Acknowledgements/LICENCE
MAMMOGRAPHIC IMAGE ANALYSIS SOCIETY
MiniMammographic Database
LICENCE AGREEMENT
This is a legal agreement between you, the end user and the
Mammographic Image Analysis Society ("MIAS"). Upon installing the
MiniMammographic database (the "DATABASE") on your system you are
agreeing to be bound by the terms of this Agreement.

## GRANT OF LICENCE
MIAS grants you the right to use the DATABASE, for research purposes
ONLY. For this purpose, you may edit, format, or otherwise modify the
DATABASE provided that the unmodified portions of the DATABASE included
in a modified work shall remain subject to the terms of this Agreement.
COPYRIGHT
The DATABASE is owned by MIAS and is protected by United Kingdom
copyright laws, international treaty provisions and all other
applicable national laws. Therefore you must treat the DATABASE
like any other copyrighted material. If the DATABASE is used in any
publications then reference must be made to the DATABASE within that
publication.
## OTHER RESTRICTIONS
You may not rent, lease or sell the DATABASE.
LIABILITY
To the maximum extent permitted by applicable law, MIAS shall not
be liable for damages, other than death or personal injury,
whatsoever (including without limitation, damages for negligence,
loss of business, profits, business interruption, loss of
business information, or other pecuniary loss) arising out of the
use of or inability to use this DATABASE, even if MIAS has been
advised of the possibility of such damages. In any case, MIAS's
entire liability under this Agreement shall be limited to the
amount actually paid by you or your assignor, as the case may be,
for the DATABASE.
## Inspiration
Automatically finding lesions would be a very helpful tool for physicians, also predicting malignancy based on a found/marked lesion
