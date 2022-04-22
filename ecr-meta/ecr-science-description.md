# Science
To be filled

# AI@Edge
The application takes LiDAR data from miniMPL instrument and converts the binary data into time-series array representing cloud heights of the target region. First it attempts to download data from the sensor, then calculates cloud height from the data.

# Using the code
Output: cloud height of the target region
Input: binary blob of MPL LiDAR data

# Arguments
   `-debug`: Debug flag
   `-stream`: ID or name of a stream, e.g. bottom-camera  
   `-object`: Object name to count  
   `-all-objects`: Consider all registered objects to detect (default = False)  
   `-model`: Path to model (default = `coco_ssd_resnet50_300_fp32.pth`)  
   `-image-size`: Input image size (default = 0.4)  
   `-confidence-level`: Confidence level [0. - 1.] to filter out result  
   `-interval`: Inference interval in seconds (default = 0, no interval)  
   `-sampling-interval`: Sampling interval between inferencing (default = -1, no sampling)  

# Ontology
The code publishes measurements with topic `env.height.cloud` representing cloud height in killometer.

# Inference from Sage codes
To query the output from the plugin, you can do with python library 'sage_data_client':
```
import sage_data_client

# query and load data into pandas data frame
df = sage_data_client.query(
    start="-1h",
    filter={
        "name": "env.height.cloud",
    }
)

# print results in data frame
print(df)
```
For more information, please see [Access and use data documentation](https://docs.sagecontinuum.org/docs/tutorials/accessing-data) and [sage_data_client](https://pypi.org/project/sage-data-client/).
