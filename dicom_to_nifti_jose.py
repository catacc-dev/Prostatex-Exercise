import SimpleITK as sitk
import pydicom
import argparse


def convert_to_sitk(dcm_dir: str) -> sitk.Image:
    """
    Convert dicom series to sitk image.

    Args:
        dcm_dir (str): directory containing dicom series.

    Returns:
        sitk.Image: sitk Image.
    """
    reader = sitk.ImageSeriesReader()

    dicom_names = reader.GetGDCMSeriesFileNames(dcm_dir)
    if (0x0019, 0x100C) in pydicom.dcmread(dicom_names[0]):
        new_dicom_names = []
        for dicom_name in dicom_names:
            b_value = pydicom.dcmread(dicom_name)[0x0019, 0x100C].value
            if isinstance(b_value, bytes):
                b_value = b_value.decode()
            if isinstance(b_value, str):
                b_value = int(b_value)
            if b_value == 50:
                new_dicom_names.append(dicom_name)
        dicom_names = new_dicom_names
    reader.SetFileNames(dicom_names)

    image = reader.Execute()

    return image


def main():
    parser = argparse.ArgumentParser(description='Convert DICOM series to SimpleITK image.')
    parser.add_argument('dcm_dir', type=str, help='Directory containing DICOM series.')
    parser.add_argument('output_sitk', type=str, help='Output filename for the SimpleITK image.')

    args = parser.parse_args()

    # Call the conversion function
    sitk_image = convert_to_sitk(args.dcm_dir)

    # Write the output image
    sitk.WriteImage(sitk_image, args.output_sitk)
    print(f'Successfully converted DICOM series from {args.dcm_dir} to {args.output_sitk}')


if __name__ == "__main__":
    main()

# to run it:
#python convert_dicom.py <dcm_dir> <output_sitk>
