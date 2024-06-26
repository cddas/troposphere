# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean
from .validators.iot1click import validate_json_checker


class Device(AWSObject):
    """
    `Device <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html>`__
    """

    resource_type = "AWS::IoT1Click::Device"

    props: PropsDictType = {
        "DeviceId": (str, True),
        "Enabled": (boolean, True),
    }


class Placement(AWSObject):
    """
    `Placement <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html>`__
    """

    resource_type = "AWS::IoT1Click::Placement"

    props: PropsDictType = {
        "AssociatedDevices": (validate_json_checker, False),
        "Attributes": (validate_json_checker, False),
        "PlacementName": (str, False),
        "ProjectName": (str, True),
    }


class PlacementTemplate(AWSProperty):
    """
    `PlacementTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-placementtemplate.html>`__
    """

    props: PropsDictType = {
        "DefaultAttributes": (validate_json_checker, False),
        "DeviceTemplates": (validate_json_checker, False),
    }


class Project(AWSObject):
    """
    `Project <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html>`__
    """

    resource_type = "AWS::IoT1Click::Project"

    props: PropsDictType = {
        "Description": (str, False),
        "PlacementTemplate": (PlacementTemplate, True),
        "ProjectName": (str, False),
    }


class DeviceTemplate(AWSProperty):
    """
    `DeviceTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iot1click-project-devicetemplate.html>`__
    """

    props: PropsDictType = {
        "CallbackOverrides": (dict, False),
        "DeviceType": (str, False),
    }
