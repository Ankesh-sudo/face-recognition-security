import cv2
import os

DATASET_PATH = "data/known_faces"

def register_user(username):
    user_dir = os.path.join(DATASET_PATH, username)
    os.makedirs(user_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    count = 0

    print("📸 Capturing face images. Press 'q' to stop.")

    while count < 20:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Register Face", frame)

        img_path = os.path.join(user_dir, f"{count}.jpg")
        cv2.imwrite(img_path, frame)
        count += 1

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"✅ {count} images saved for user: {username}")


if __name__ == "__main__":
    name = input("Enter username: ")
    register_user(name)
