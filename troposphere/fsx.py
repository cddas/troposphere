# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.fsx import (
    storage_type,
    validate_lustreconfiguration,
    validate_lustreconfiguration_deploymenttype,
    validate_lustreconfiguration_perunitstoragethroughput,
)


class AutoExportPolicy(AWSProperty):
    """
    `AutoExportPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-autoexportpolicy.html>`__
    """

    props: PropsDictType = {
        "Events": ([str], True),
    }


class AutoImportPolicy(AWSProperty):
    """
    `AutoImportPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-autoimportpolicy.html>`__
    """

    props: PropsDictType = {
        "Events": ([str], True),
    }


class S3(AWSProperty):
    """
    `S3 <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-datarepositoryassociation-s3.html>`__
    """

    props: PropsDictType = {
        "AutoExportPolicy": (AutoExportPolicy, False),
        "AutoImportPolicy": (AutoImportPolicy, False),
    }


class DataRepositoryAssociation(AWSObject):
    """
    `DataRepositoryAssociation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-datarepositoryassociation.html>`__
    """

    resource_type = "AWS::FSx::DataRepositoryAssociation"

    props: PropsDictType = {
        "BatchImportMetaDataOnCreate": (boolean, False),
        "DataRepositoryPath": (str, True),
        "FileSystemId": (str, True),
        "FileSystemPath": (str, True),
        "ImportedFileChunkSize": (integer, False),
        "S3": (S3, False),
        "Tags": (Tags, False),
    }


class MetadataConfiguration(AWSProperty):
    """
    `MetadataConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration-metadataconfiguration.html>`__
    """

    props: PropsDictType = {
        "Iops": (integer, False),
        "Mode": (str, False),
    }


class LustreConfiguration(AWSProperty):
    """
    `LustreConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-lustreconfiguration.html>`__
    """

    props: PropsDictType = {
        "AutoImportPolicy": (str, False),
        "AutomaticBackupRetentionDays": (integer, False),
        "CopyTagsToBackups": (boolean, False),
        "DailyAutomaticBackupStartTime": (str, False),
        "DataCompressionType": (str, False),
        "DeploymentType": (validate_lustreconfiguration_deploymenttype, False),
        "DriveCacheType": (str, False),
        "ExportPath": (str, False),
        "ImportPath": (str, False),
        "ImportedFileChunkSize": (integer, False),
        "MetadataConfiguration": (MetadataConfiguration, False),
        "PerUnitStorageThroughput": (
            validate_lustreconfiguration_perunitstoragethroughput,
            False,
        ),
        "WeeklyMaintenanceStartTime": (str, False),
    }

    def validate(self):
        validate_lustreconfiguration(self)


class DiskIopsConfiguration(AWSProperty):
    """
    `DiskIopsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-diskiopsconfiguration.html>`__
    """

    props: PropsDictType = {
        "Iops": (integer, False),
        "Mode": (str, False),
    }


class OntapConfiguration(AWSProperty):
    """
    `OntapConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-ontapconfiguration.html>`__
    """

    props: PropsDictType = {
        "AutomaticBackupRetentionDays": (integer, False),
        "DailyAutomaticBackupStartTime": (str, False),
        "DeploymentType": (str, True),
        "DiskIopsConfiguration": (DiskIopsConfiguration, False),
        "EndpointIpAddressRange": (str, False),
        "FsxAdminPassword": (str, False),
        "HAPairs": (integer, False),
        "PreferredSubnetId": (str, False),
        "RouteTableIds": ([str], False),
        "ThroughputCapacity": (integer, False),
        "ThroughputCapacityPerHAPair": (integer, False),
        "WeeklyMaintenanceStartTime": (str, False),
    }


class ClientConfigurations(AWSProperty):
    """
    `ClientConfigurations <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports-clientconfigurations.html>`__
    """

    props: PropsDictType = {
        "Clients": (str, True),
        "Options": ([str], True),
    }


class NfsExports(AWSProperty):
    """
    `NfsExports <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-nfsexports.html>`__
    """

    props: PropsDictType = {
        "ClientConfigurations": ([ClientConfigurations], True),
    }


class UserAndGroupQuotas(AWSProperty):
    """
    `UserAndGroupQuotas <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-userandgroupquotas.html>`__
    """

    props: PropsDictType = {
        "Id": (integer, True),
        "StorageCapacityQuotaGiB": (integer, True),
        "Type": (str, True),
    }


class RootVolumeConfiguration(AWSProperty):
    """
    `RootVolumeConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration-rootvolumeconfiguration.html>`__
    """

    props: PropsDictType = {
        "CopyTagsToSnapshots": (boolean, False),
        "DataCompressionType": (str, False),
        "NfsExports": ([NfsExports], False),
        "ReadOnly": (boolean, False),
        "RecordSizeKiB": (integer, False),
        "UserAndGroupQuotas": ([UserAndGroupQuotas], False),
    }


class OpenZFSConfiguration(AWSProperty):
    """
    `OpenZFSConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-openzfsconfiguration.html>`__
    """

    props: PropsDictType = {
        "AutomaticBackupRetentionDays": (integer, False),
        "CopyTagsToBackups": (boolean, False),
        "CopyTagsToVolumes": (boolean, False),
        "DailyAutomaticBackupStartTime": (str, False),
        "DeploymentType": (str, True),
        "DiskIopsConfiguration": (DiskIopsConfiguration, False),
        "EndpointIpAddressRange": (str, False),
        "Options": ([str], False),
        "PreferredSubnetId": (str, False),
        "RootVolumeConfiguration": (RootVolumeConfiguration, False),
        "RouteTableIds": ([str], False),
        "ThroughputCapacity": (integer, False),
        "WeeklyMaintenanceStartTime": (str, False),
    }


class AuditLogConfiguration(AWSProperty):
    """
    `AuditLogConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration-auditlogconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuditLogDestination": (str, False),
        "FileAccessAuditLogLevel": (str, True),
        "FileShareAccessAuditLogLevel": (str, True),
    }


class SelfManagedActiveDirectoryConfiguration(AWSProperty):
    """
    `SelfManagedActiveDirectoryConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration-selfmanagedactivedirectoryconfiguration.html>`__
    """

    props: PropsDictType = {
        "DnsIps": ([str], False),
        "DomainName": (str, False),
        "FileSystemAdministratorsGroup": (str, False),
        "OrganizationalUnitDistinguishedName": (str, False),
        "Password": (str, False),
        "UserName": (str, False),
    }


class WindowsConfiguration(AWSProperty):
    """
    `WindowsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-filesystem-windowsconfiguration.html>`__
    """

    props: PropsDictType = {
        "ActiveDirectoryId": (str, False),
        "Aliases": ([str], False),
        "AuditLogConfiguration": (AuditLogConfiguration, False),
        "AutomaticBackupRetentionDays": (integer, False),
        "CopyTagsToBackups": (boolean, False),
        "DailyAutomaticBackupStartTime": (str, False),
        "DeploymentType": (str, False),
        "DiskIopsConfiguration": (DiskIopsConfiguration, False),
        "PreferredSubnetId": (str, False),
        "SelfManagedActiveDirectoryConfiguration": (
            SelfManagedActiveDirectoryConfiguration,
            False,
        ),
        "ThroughputCapacity": (integer, True),
        "WeeklyMaintenanceStartTime": (str, False),
    }


class FileSystem(AWSObject):
    """
    `FileSystem <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html>`__
    """

    resource_type = "AWS::FSx::FileSystem"

    props: PropsDictType = {
        "BackupId": (str, False),
        "FileSystemType": (str, True),
        "FileSystemTypeVersion": (str, False),
        "KmsKeyId": (str, False),
        "LustreConfiguration": (LustreConfiguration, False),
        "OntapConfiguration": (OntapConfiguration, False),
        "OpenZFSConfiguration": (OpenZFSConfiguration, False),
        "SecurityGroupIds": ([str], False),
        "StorageCapacity": (integer, False),
        "StorageType": (storage_type, False),
        "SubnetIds": ([str], True),
        "Tags": (Tags, False),
        "WindowsConfiguration": (WindowsConfiguration, False),
    }


class Snapshot(AWSObject):
    """
    `Snapshot <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-snapshot.html>`__
    """

    resource_type = "AWS::FSx::Snapshot"

    props: PropsDictType = {
        "Name": (str, True),
        "Tags": (Tags, False),
        "VolumeId": (str, True),
    }


class ActiveDirectoryConfiguration(AWSProperty):
    """
    `ActiveDirectoryConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-storagevirtualmachine-activedirectoryconfiguration.html>`__
    """

    props: PropsDictType = {
        "NetBiosName": (str, False),
        "SelfManagedActiveDirectoryConfiguration": (
            SelfManagedActiveDirectoryConfiguration,
            False,
        ),
    }


class StorageVirtualMachine(AWSObject):
    """
    `StorageVirtualMachine <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-storagevirtualmachine.html>`__
    """

    resource_type = "AWS::FSx::StorageVirtualMachine"

    props: PropsDictType = {
        "ActiveDirectoryConfiguration": (ActiveDirectoryConfiguration, False),
        "FileSystemId": (str, True),
        "Name": (str, True),
        "RootVolumeSecurityStyle": (str, False),
        "SvmAdminPassword": (str, False),
        "Tags": (Tags, False),
    }


class AggregateConfiguration(AWSProperty):
    """
    `AggregateConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-aggregateconfiguration.html>`__
    """

    props: PropsDictType = {
        "Aggregates": ([str], False),
        "ConstituentsPerAggregate": (integer, False),
    }


class AutocommitPeriod(AWSProperty):
    """
    `AutocommitPeriod <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration-autocommitperiod.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (integer, False),
    }


class RetentionPeriod(AWSProperty):
    """
    `RetentionPeriod <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-retentionperiod.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (integer, False),
    }


class SnaplockRetentionPeriod(AWSProperty):
    """
    `SnaplockRetentionPeriod <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-snaplockretentionperiod.html>`__
    """

    props: PropsDictType = {
        "DefaultRetention": (RetentionPeriod, True),
        "MaximumRetention": (RetentionPeriod, True),
        "MinimumRetention": (RetentionPeriod, True),
    }


class SnaplockConfiguration(AWSProperty):
    """
    `SnaplockConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-snaplockconfiguration.html>`__
    """

    props: PropsDictType = {
        "AuditLogVolume": (str, False),
        "AutocommitPeriod": (AutocommitPeriod, False),
        "PrivilegedDelete": (str, False),
        "RetentionPeriod": (SnaplockRetentionPeriod, False),
        "SnaplockType": (str, True),
        "VolumeAppendModeEnabled": (str, False),
    }


class TieringPolicy(AWSProperty):
    """
    `TieringPolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration-tieringpolicy.html>`__
    """

    props: PropsDictType = {
        "CoolingPeriod": (integer, False),
        "Name": (str, False),
    }


class VolumeOntapConfiguration(AWSProperty):
    """
    `VolumeOntapConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-ontapconfiguration.html>`__
    """

    props: PropsDictType = {
        "AggregateConfiguration": (AggregateConfiguration, False),
        "CopyTagsToBackups": (str, False),
        "JunctionPath": (str, False),
        "OntapVolumeType": (str, False),
        "SecurityStyle": (str, False),
        "SizeInBytes": (str, False),
        "SizeInMegabytes": (str, False),
        "SnaplockConfiguration": (SnaplockConfiguration, False),
        "SnapshotPolicy": (str, False),
        "StorageEfficiencyEnabled": (str, False),
        "StorageVirtualMachineId": (str, True),
        "TieringPolicy": (TieringPolicy, False),
        "VolumeStyle": (str, False),
    }


class OriginSnapshot(AWSProperty):
    """
    `OriginSnapshot <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration-originsnapshot.html>`__
    """

    props: PropsDictType = {
        "CopyStrategy": (str, True),
        "SnapshotARN": (str, True),
    }


class VolumeOpenZFSConfiguration(AWSProperty):
    """
    `VolumeOpenZFSConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fsx-volume-openzfsconfiguration.html>`__
    """

    props: PropsDictType = {
        "CopyTagsToSnapshots": (boolean, False),
        "DataCompressionType": (str, False),
        "NfsExports": ([NfsExports], False),
        "Options": ([str], False),
        "OriginSnapshot": (OriginSnapshot, False),
        "ParentVolumeId": (str, True),
        "ReadOnly": (boolean, False),
        "RecordSizeKiB": (integer, False),
        "StorageCapacityQuotaGiB": (integer, False),
        "StorageCapacityReservationGiB": (integer, False),
        "UserAndGroupQuotas": ([UserAndGroupQuotas], False),
    }


class Volume(AWSObject):
    """
    `Volume <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-volume.html>`__
    """

    resource_type = "AWS::FSx::Volume"

    props: PropsDictType = {
        "BackupId": (str, False),
        "Name": (str, True),
        "OntapConfiguration": (VolumeOntapConfiguration, False),
        "OpenZFSConfiguration": (VolumeOpenZFSConfiguration, False),
        "Tags": (Tags, False),
        "VolumeType": (str, False),
    }
