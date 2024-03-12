import cv2

def main():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)  # '0' is usually the default ID for the first webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Set frame width and height (optional, depending on your needs)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the resulting frame
        cv2.imshow('Webcam Live', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
