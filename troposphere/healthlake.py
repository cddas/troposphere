# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, PropsDictType, Tags


class PreloadDataConfig(AWSProperty):
    """
    `PreloadDataConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html>`__
    """

    props: PropsDictType = {
        "PreloadDataType": (str, True),
    }


class KmsEncryptionConfig(AWSProperty):
    """
    `KmsEncryptionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html>`__
    """

    props: PropsDictType = {
        "CmkType": (str, True),
        "KmsKeyId": (str, False),
    }


class SseConfiguration(AWSProperty):
    """
    `SseConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html>`__
    """

    props: PropsDictType = {
        "KmsEncryptionConfig": (KmsEncryptionConfig, True),
    }


class FHIRDatastore(AWSObject):
    """
    `FHIRDatastore <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html>`__
    """

    resource_type = "AWS::HealthLake::FHIRDatastore"

    props: PropsDictType = {
        "DatastoreName": (str, False),
        "DatastoreTypeVersion": (str, True),
        "PreloadDataConfig": (PreloadDataConfig, False),
        "SseConfiguration": (SseConfiguration, False),
        "Tags": (Tags, False),
    }
