import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

input_folder = r"C:\Users\Wikaa\Desktop\Uczelnia-notatki\5_semestr\podstawy_programowania_aplikacji_gis\projekt_zaliczeniowy_WH_AS\dane\powiat_sztumski_NMT"
output_raster = r"C:\Users\Wikaa\Desktop\Uczelnia-notatki\5_semestr\podstawy_programowania_aplikacji_gis\projekt_zaliczeniowy_WH_AS\dane\wynikowe\rasterWynikowy.tif"

arcpy.env.workspace = input_folder
rasters = arcpy.ListRasters()

if len(rasters) < 2:
    raise Exception("Potrzebne są co najmniej dwa rastry do połączenia.")

arcpy.management.MosaicToNewRaster(
    input_rasters=rasters,
    output_location=input_folder,
    raster_dataset_name_with_extension=output_raster.split("\\")[-1],
    coordinate_system_for_the_raster="",
    pixel_type="32_BIT_FLOAT",  
    cellsize="",
    number_of_bands=1,  
    mosaic_method="BLEND",
    mosaic_colormap_mode="FIRST"
)

print(f"Rastry zostały połączone i zapisane jako: {output_raster}")