# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class ConnectionAlias(AWSObject):
    """
    `ConnectionAlias <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html>`__
    """

    resource_type = "AWS::WorkSpaces::ConnectionAlias"

    props: PropsDictType = {
        "ConnectionString": (str, True),
        "Tags": (Tags, False),
    }


class WorkspaceProperties(AWSProperty):
    """
    `WorkspaceProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html>`__
    """

    props: PropsDictType = {
        "ComputeTypeName": (str, False),
        "RootVolumeSizeGib": (integer, False),
        "RunningMode": (str, False),
        "RunningModeAutoStopTimeoutInMinutes": (integer, False),
        "UserVolumeSizeGib": (integer, False),
    }


class Workspace(AWSObject):
    """
    `Workspace <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html>`__
    """

    resource_type = "AWS::WorkSpaces::Workspace"

    props: PropsDictType = {
        "BundleId": (str, True),
        "DirectoryId": (str, True),
        "RootVolumeEncryptionEnabled": (boolean, False),
        "Tags": (Tags, False),
        "UserName": (str, True),
        "UserVolumeEncryptionEnabled": (boolean, False),
        "VolumeEncryptionKey": (str, False),
        "WorkspaceProperties": (WorkspaceProperties, False),
    }
