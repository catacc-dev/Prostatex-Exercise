import SimpleITK as sitk
import pydicom as dicom
import os

# EXERCISE 6 AND 7
def convertingDicomtoNifti(dicom_directory_path, output_file):

    #dicom_directory_path = "C:\\Users\\catar\\PROSTATEX\\manifest-A3Y4AE4o5818678569166032044\\PROSTATEx\\ProstateX-0006\\10-21-2011-NA-MR prostaat kanker detectie NDmc MCAPRODETN-79408\\3.000000-t2tsesag-19869"
    input_path = os.path.realpath(dicom_directory_path)

    print("Reading Dicom directory:", input_path)

    reader = sitk.ImageSeriesReader()

    dicom_names = reader.GetGDCMSeriesFileNames(input_path)
    reader.SetFileNames(dicom_names)

    image = reader.Execute()

    for dicom_file in dicom_names:
        ds = dicom.dcmread(dicom_file)
        elem_position = ds[0x0020, 0x0032]  # Image position
        elem_orientation = ds[0x0020, 0x0037]  # Image orientation
        print(f"File: {dicom_file}")
        print(f"Image position: {elem_position} and Image orientation: {elem_orientation}")


    #print("Writing image:", output_file)

    sitk.WriteImage(image, output_file)

    # Downloaded ImageJ and opened there the "output_image.nii.gz"

    return image


prostatex = "C:\\Users\\catar\\PROSTATEX\\manifest-A3Y4AE4o5818678569166032044\\PROSTATEx"

for patient in os.listdir(prostatex):
    study_folder = os.path.join(prostatex, patient)
    # Check if study_folder is a valid directory
    if not os.path.isdir(study_folder):
        continue
    
    for study in os.listdir(study_folder):
        series_folder = os.path.join(study_folder, study)
        # Check if series_folder is a valid directory
        if not os.path.isdir(series_folder):
            continue
        
        for series in os.listdir(series_folder):
            dicom_directory = os.path.join(series_folder, series)

            # Ensure dicom_directory is a valid directory
            if os.path.isdir(dicom_directory):

                output_nifti_file = os.path.join(
                    "C:\\Users\\catar\\Prostatex-Exercise",
                    f"{patient}_{study}_{series}.nii.gz"
                )

                image_volume = convertingDicomtoNifti(dicom_directory, output_nifti_file)

                if image_volume:
                    print("Successfully converted:", output_nifti_file)
                else:
                    print("Conversion failed for:", dicom_directory)
            else:
                print(f"Skipping non-directory file: {dicom_directory}")
    