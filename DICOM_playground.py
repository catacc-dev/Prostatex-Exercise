
import pydicom as dicom
import matplotlib.pylab as plt

# PROSTATEx dataset - downloaded images from 75 subjects, each suject has done x MRI series and each MRI series contains multiple slices

# Specify your image path
image_path = "C:\\Users\\catar\\PROSTATEX\\manifest-A3Y4AE4o5818678569166032044\\PROSTATEx\\ProstateX-0000\\07-07-2011-NA-MR prostaat kanker detectie WDSmc MCAPRODETW-05711\\3.000000-t2tsesag-87368\\1-07.dcm"
ds = dicom.dcmread(image_path)

# Hierarchy of DICOM: Patient; Study; Series; Instance
# INSTANCE = DICOM FILE

# EXERCISE 1
#print(ds)

# Check if pixel_array is valid
# print(ds.pixel_array.shape)

# EXERCISE 2
#plt.imshow(ds.pixel_array,cmap='gray')
#plt.show() # Display the image

# EXERCISE 3
#print(ds.file_meta)

# EXERCISE 4
#elem = ds[0x0020, 0x000D]
#print(elem) # (0020,000D) Study Instance UID                  UI: 1.3.6.1.4.1.14519.5.2.1.7311.5101.158323547117540061132729905711

#elem = ds[0x0020, 0x000E]
#print(elem) # (0020,000E) Series Instance UID                 UI: 1.3.6.1.4.1.14519.5.2.1.7311.5101.250911858840767891342974687368

#elem = ds[0x0020, 0x0032]
#print(elem) # (0020,0032) Image Position (Patient)            DS: [28.162851333618, -66.736778259277, 56.274690240622]

#elem = ds[0x0020, 0x0037]
#print(elem) # (0020,0037) Image Orientation (Patient)         DS: [0, 1, 0, 0, 0, -1]

#elem = ds[0x0018, 0x0088]
#print(elem) # (0018,0088) Spacing Between Slices              DS: '3.6'

#elem = ds[0x0028, 0x0030]
#print(elem) # (0028,0030) Pixel Spacing                       DS: [0.5625, 0.5625]

#elem = ds[0x0018, 0x9087] # not present in this example

#elem = ds[0x0008, 0x1030]
#print(elem) # (0008,1030) Study Description                   LO: 'MR prostaat kanker detectie WDS_mc MCAPRODETW'

#elem = ds[0x0008, 0x103E]
#print(elem) # (0008,103E) Series Description                  LO: 't2_tse_sag'

# EXERCISE 5
folder_path = "C:\\Users\\catar\\PROSTATEX\\manifest-A3Y4AE4o5818678569166032044\\PROSTATEx\\ProstateX-0006\\10-21-2011-NA-MR prostaat kanker detectie NDmc MCAPRODETN-79408\\3.000000-t2tsesag-19869"
folder_path = os.path.realpath(folder_path) # SERIES

dicom_files = []
for image_name in os.listdir(folder_path): # INSTANCES=SLICES
    image_path = os.path.join(folder_path, image_name)
    ds_files = dicom.dcmread(image_path)
    dicom_files.append(ds_files)

# Sort the slices by Instance Number - ascending order
#dicom_files.sort(key=lambda x: int(x.InstanceNumber)) # key-comparison is based on this function; lambda input_variable(s): tasty one liner
# OR
# Sort by the third value in the position tuple ImagePositionPatient - ascending order
dicom_files.sort(key=lambda x: int(x.ImagePositionPatient[2]))

# Display the ordered slices
fig, axes = plt.subplots(1, len(dicom_files))
for i, ds in enumerate(dicom_files):
    axes[i].imshow(ds.pixel_array, cmap="gray")
    axes[i].axis("off")
plt.show()
    
