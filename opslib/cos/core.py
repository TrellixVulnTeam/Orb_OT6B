'''
cos.core

Version Notes
    1.0
        First Commit
'''
import qcloud_cos
import requests


class COSClient():
    def __init__(self, client):
        self.__client = client

    def create_bucket(self, bucket_name, **kwargs) -> None:
        '''创建一个存储桶

        :param bucket_name(string): 存储桶名称
        :param kwargs(dict): 设置请求headers

        :return: None.
        '''
        self.__client.create_bucket(bucket_name, **kwargs)

    def get_buckets(self) -> dict:
        '''列出所有bucket

        :return(dict): 账号下bucket相关信息.
        '''
        return self.__client.list_buckets()

    def simple_uploadFile(self, filename, bucket, key, mode = 'rb', storageClass = 'STANDARD', enableMD5 = False) -> dict:
        """本地文件上传接口，适用于小文件，最大不得超过5GB

        :param Bucket(string): 存储桶名称.
        :param LocalFilePath(string): 上传文件的本地路径.
        :param Key(string): COS路径.
        :param EnableMD5(bool): 是否需要SDK计算Content-MD5，打开此开关会增加上传耗时.
        :kwargs(dict): 设置上传的headers.

        :return(dict): 上传成功返回的结果，包含ETag等信息.
        """
        with open(filename, mode) as fp:
            response = self.__client.put_object(
                Bucket = bucket,
                Body = fp,
                Key = key,
                StorageClass = storageClass,
                EnableMD5 = enableMD5
            )
        return response
    
    def simple_upload(self, body, bucket, key, storageClass = 'STANDARD', enableMD5 = False) -> dict:
        """本地文件上传接口，适用于小文件，最大不得超过5GB

        :param Bucket(string): 存储桶名称.
        :param LocalFilePath(string): 上传文件的本地路径.
        :param Key(string): COS路径.
        :param EnableMD5(bool): 是否需要SDK计算Content-MD5，打开此开关会增加上传耗时.
        :kwargs(dict): 设置上传的headers.

        :return(dict): 上传成功返回的结果，包含ETag等信息.
        """
        return self.__client.put_object(
            Bucket = bucket,
            Body = body,
            Key = key,
            StorageClass = storageClass,
            EnableMD5 = enableMD5
        )

    def get_filesList(self, bucket, prefix = '', delimiter = '',marker = '', maxKeys = 1000, encodingType = '', **kwargs) -> list:
        '''获取文件列表

        :param Bucket(string): 存储桶名称.
        :param Prefix(string): 设置匹配文件的前缀.
        :param Delimiter(string): 分隔符.
        :param Marker(string): 从marker开始列出条目.
        :param MaxKeys(int): 设置单次返回最大的数量,最大为1000.
        :param EncodingType(string): 设置返回结果编码方式,只能设置为url.
        :param kwargs(dict): 设置请求headers.
        :return(dict): 文件的相关信息，包括Etag等信息.


        .. code-block:: python
        config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
        client = CosS3Client(config)
        # 列出bucket
        response = client.list_objects(
            Bucket='bucket',
            MaxKeys=100,
            Prefix='中文',
            Delimiter='/'
        )
        '''
        files = []
        while True:
            response = self.__client.list_objects(
                Bucket = bucket,
                Prefix = prefix,
                Delimiter = delimiter,
                MaxKeys = maxKeys,
                Marker = marker,
                EncodingType = encodingType,
                **kwargs
            )
            files.extend(response['Contents'])
            if response['IsTruncated'] == 'false':
                break
            marker = response['NextMarker']
        return files


