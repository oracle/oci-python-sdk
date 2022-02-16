# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .audio_format_details import AudioFormatDetails
from .change_transcription_job_compartment_details import ChangeTranscriptionJobCompartmentDetails
from .create_transcription_job_details import CreateTranscriptionJobDetails
from .input_location import InputLocation
from .object_list_file_input_location import ObjectListFileInputLocation
from .object_list_inline_input_location import ObjectListInlineInputLocation
from .object_location import ObjectLocation
from .output_location import OutputLocation
from .profanity_transcription_filter import ProfanityTranscriptionFilter
from .transcription_filter import TranscriptionFilter
from .transcription_job import TranscriptionJob
from .transcription_job_collection import TranscriptionJobCollection
from .transcription_job_summary import TranscriptionJobSummary
from .transcription_model_details import TranscriptionModelDetails
from .transcription_normalization import TranscriptionNormalization
from .transcription_task import TranscriptionTask
from .transcription_task_collection import TranscriptionTaskCollection
from .transcription_task_summary import TranscriptionTaskSummary
from .update_transcription_job_details import UpdateTranscriptionJobDetails

# Maps type names to classes for ai_speech services.
ai_speech_type_mapping = {
    "AudioFormatDetails": AudioFormatDetails,
    "ChangeTranscriptionJobCompartmentDetails": ChangeTranscriptionJobCompartmentDetails,
    "CreateTranscriptionJobDetails": CreateTranscriptionJobDetails,
    "InputLocation": InputLocation,
    "ObjectListFileInputLocation": ObjectListFileInputLocation,
    "ObjectListInlineInputLocation": ObjectListInlineInputLocation,
    "ObjectLocation": ObjectLocation,
    "OutputLocation": OutputLocation,
    "ProfanityTranscriptionFilter": ProfanityTranscriptionFilter,
    "TranscriptionFilter": TranscriptionFilter,
    "TranscriptionJob": TranscriptionJob,
    "TranscriptionJobCollection": TranscriptionJobCollection,
    "TranscriptionJobSummary": TranscriptionJobSummary,
    "TranscriptionModelDetails": TranscriptionModelDetails,
    "TranscriptionNormalization": TranscriptionNormalization,
    "TranscriptionTask": TranscriptionTask,
    "TranscriptionTaskCollection": TranscriptionTaskCollection,
    "TranscriptionTaskSummary": TranscriptionTaskSummary,
    "UpdateTranscriptionJobDetails": UpdateTranscriptionJobDetails
}
