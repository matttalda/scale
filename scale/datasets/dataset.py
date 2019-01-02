"""Manages the DataSet definition schema"""
from __future__ import unicode_literals

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from dataset.exceptions import InvalidDataSetDefinition()

SCHEMA_VERSION = '6'
DATA_SET_DEFINITIONA_SCHEMA = {
    'type': 'object',
    'required': ['definition'],
    'additionalProperties': False,
    'properties': {
        'version': {
            'description': 'Version of the dataset schema',
            'type': 'string',
            'pattern': '^.{0,50}$',
        },
        'definition': {
            'description': 'The data',
            'type': 'object',
        }
    }
}


def convert_definition_to_v6_json(definition):
    """Returns the v6 dataset definition JSON for the given definition
    
    :param definition: The dataset definition
    :type definition: :class:`??`
    :returns: The v6 dataset definition JSON
    :rtype: :class:`dataset.DataSetDefinition
    """
    
    def_dict={
        'version': SCHEMA_VERSION,
        'definition': definition.definition
    }
    
    return DataSetDefinition(definition=def_dict, do_validate=False)


class DataSetDefinition(object):
    """
    Represents the definition of a DataSet object
    
    :keyword title: The title of this data set (optional)
    :type title: :class:`django.db.models.CharField`
    :keyword description: The description of the data set (optional)
    :type description: :class:`django.db.models.CharField`
    :keyword created_time:
    :type created_time: :class:`django.db.models.DateTimeField`
    """
    def __init__(self, definition=None, do_validate=True):
        """Constructor
        """
        
        if not definition:
            definition = {}
        self._definition = definition
        
        if 'version' not in self._definition:
            self._definition['version'] = SCHEMA_VERSION
            
        if self._definition['version'] != SCHEMA_VERSION:
            self
            
        self._populate_default_values()
        
        try:
            if do_validate:
                validate(definition, DATA_SET_DEFINITIONA_SCHEMA)
        except ValidationError as validation_error:
            raise InvalidDataSetDefinition(validation_error)
        
    def get_definition_dict(self):
        """Returns the dict of the definition
        """
 
        
        
    def _populate_default_values(self):
        """Populates any missing JSON fields that have default values
        """
