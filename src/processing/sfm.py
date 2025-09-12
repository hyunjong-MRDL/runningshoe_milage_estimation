import cv2

def feature_detection_and_matching(img_path1, img_path2):
    sift = cv2.SIFT_create()

    img1 = cv2.imread(img_path1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img_path2, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        print("이미지 로딩 에러: 이미지 경로를 다시 확인하세요.")
        return None
    
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)
    
    return matches, kp1, kp2

if __name__ == "__main__":
    from pathlib import Path

    cwd = Path.cwd()
    processed_root = cwd / r"data/processed"
    processed_data = [f for f in processed_root.iterdir() if f.is_file()]

    if len(processed_data) >= 2:
        img_path1 = str(processed_data[0])
        img_path2 = str(processed_data[1])

        matches, kp1, kp2 = feature_detection_and_matching(img_path1, img_path2)

        if matches:
            print(f"Total matches found: {len(matches)}")
            print("Top 10 matches:")
            for m in matches[:10]:
                print(f"Match distance: {m.distance}")
            
            img1 = cv2.imread(img_path1)
            img2 = cv2.imread(img_path2)

            draw_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            cv2.imshow("Matches", draw_matches)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    
    else:
        print("이미지 부족: 특징점 비교를 위해 이미지가 2장 이상 필요합니다.")