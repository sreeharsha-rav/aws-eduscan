import os
import pickle
import face_recognition

# Function to read the 'encoding' file
def open_encoding(filename):
	file = open(filename, "rb")
	data = pickle.load(file)
	file.close()
	return data

# Function extracts frames from video file using ffmpeg
def extract_frames(video_path, output_dir):
	command = f"ffmpeg -i {video_path} -r 1 {output_dir}/image-%03d.jpeg"
	os.system(command)

# Function to perform face recognition on extracted frames and return the name of the matched face; O(N) time complexity
def recognize_face(output_dir):
	# boolean to check if a match is found
	isMatchFound = False
	# loop over the images in the output directory
	for image in os.listdir(output_dir):
		# check if a match is found
		if isMatchFound:
			break
		# check if the image is a jpeg file
		elif image.endswith(".jpeg"):
			image_path = os.path.join(output_dir, image)
			# load the image
			image = face_recognition.load_image_file(image_path)
			# check if there are faces in the image
			face_locations = face_recognition.face_locations(image)
			# if no faces are found, skip the image
			if len(face_locations) == 0:
				print(f"No faces found in {image_path}")
				continue
			else:
				print(f"Found {len(face_locations)} face(s) in {image_path}")
				# get face encodings for the image
				unknown_face_encodings = face_recognition.face_encodings(image)
				# load the known faces encoding file
				known_encodings = open_encoding("encoding")
				known_face_encodings = known_encodings['encoding']
				# loop over the unknown face encodings (there is only 1 face for the test cases)
				for unknown_face_encoding in unknown_face_encodings:
					# compare the faces
					results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
					# check if the face is a match
					if True in results:
						print("Face matched!")
						# get the index of the matched face
						match_index = results.index(True)
						# get the name of the matched face
						match_name = known_encodings['name'][match_index]
						# set the flag to true
						isMatchFound = True
						# break out of the loop
						break
	# return the match_names array and match_index
	return match_name

# Function to process a single video file in the input directory
def process_video(file_path, output_dir):
	# process the video file
	print(f"Processing video: {file_path}")
	# extract frames from video file
	extract_frames(file_path, output_dir)

	# perform face recognition on extracted frames
	match_name = recognize_face(output_dir)
	# return the name of the matched face
	return match_name