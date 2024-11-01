import cv2
import face_recognition
import os

# Folder path for known faces
known_images_folder = "Images"
known_faces = []
known_names = []


def GetUser(): # Load and encode faces from the folder
    match_exist = False
    matched_name = ""
    for filename in os.listdir(known_images_folder):
        if filename.endswith(".png"):
            image_path = os.path.join(known_images_folder, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)
            
            if encoding:
                known_faces.append(encoding[0])
                known_names.append(os.path.splitext(filename)[0])

    print("Known faces loaded:", known_names)

    # Load the target image
    image = cv2.imread("AnonUser.png")
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect faces and encode them in the target image
    print("Wait as we recognize faces...")
    boxes = face_recognition.face_locations(rgb, model="cnn")
    face_encodings = face_recognition.face_encodings(rgb, boxes)
    print("The boxes found in the image:", boxes)

    # Compare each face encoding found in the target image
    i = 0
    for encoding in face_encodings:
        results = face_recognition.compare_faces(known_faces, encoding, tolerance=0.6)
        print(results)
        distances = face_recognition.face_distance(known_faces, encoding)
        sortLowest = distances.tolist()
        print(distances)

        # Check for matches and add a box with name if matched
        countIndex = 0
        while countIndex < len(results):
            if results[countIndex] == True and sortLowest.index(min(sortLowest)) == countIndex:
                top, right, bottom, left = boxes[i]

                cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(image, known_names[countIndex] + " {}".format(distances[countIndex]), 
                            (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 255, 0), 2)
                matched_name = known_names[countIndex]
                match_exist = True
                break

            countIndex += 1
        i += 1
        print("loop", i)

    # Display the output image
    # cv2.imshow("Output Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    if (match_exist == False):
        matched_name = "None"

    return matched_name


# name = GetUser()

# print (name)