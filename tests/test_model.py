import unittest
import oraclebmc
import datetime

class TestModel(unittest.TestCase):

    def test_model_values(self):
        instance = self.create_instance()

        self.assertEqual('some ad', instance.availability_domain)
        self.assertEqual('some compartment', instance.compartment_id)
        self.assertEqual('some name', instance.display_name)
        self.assertEqual('some id', instance.id)
        self.assertEqual('some image', instance.image)
        self.assertEqual('bar', instance.metadata['foo'])
        self.assertEqual('some region', instance.region)
        self.assertEqual('some shape', instance.shape)
        self.assertEqual('RUNNING', instance.state)
        self.assertEqual(datetime.date(1999, 12, 31), instance.time_created)

    def test_equal(self):
        instance1 = self.create_instance()
        instance2 = self.create_instance()

        assert(instance1 == instance2)

    def test_not_equal(self):
        instance1 = self.create_instance()
        instance2 = self.create_instance()

        instance2.shape = 'some other shape'

        assert (instance1 != instance2)

    def test_equal_none(self):
        instance1 = self.create_instance()
        instance2 = None

        assert (instance1 != instance2)
        assert (instance2 != instance1)
        assert (not (instance1 == instance2))

    def test_to_string(self):
        instance = self.create_instance()

        string = instance.to_str()
        assert ('some name' in string)
        assert ('foo2' in string)
        assert ('1999' in string)

    def test_to_dict(self):
        instance = self.create_instance()
        dict = instance.to_dict()

        self.assertEqual('some ad', dict['availability_domain'])
        self.assertEqual('some compartment', dict['compartment_id'])
        self.assertEqual('some name', dict['display_name'])
        self.assertEqual('some id', dict['id'])
        self.assertEqual('some image', dict['image'])
        self.assertEqual('bar', dict['metadata']['foo'])
        self.assertEqual('some region', dict['region'])
        self.assertEqual('some shape', dict['shape'])
        self.assertEqual('RUNNING', dict['state'])
        self.assertEqual(datetime.date(1999, 12, 31), dict['time_created'])

    def test_subclass(self):
        volume_attachment = oraclebmc.models.IScsiVolumeAttachment()
        self.assertEqual('iscsi', volume_attachment.attachment_type)
        assert(hasattr(volume_attachment, 'chap_username'))
        assert (hasattr(volume_attachment, 'availability_domain'))

        volume_attachment.chap_secret = 'foo'
        volume_attachment.compartment_id = 'bar'

        self.assertEqual('foo', volume_attachment.chap_secret)
        self.assertEqual('bar', volume_attachment.compartment_id)

        dict = volume_attachment.to_dict()

        self.assertEqual('foo', dict['chap_secret'])
        self.assertEqual('bar', dict['compartment_id'])

    def create_instance(self):
        instance = oraclebmc.models.Instance()
        instance.availability_domain = 'some ad'
        instance.compartment_id = 'some compartment'
        instance.display_name = 'some name'
        instance.id = 'some id'
        instance.image = 'some image'
        instance.metadata = {'foo': 'bar', 'foo2': 'bar2'}
        instance.region = 'some region'
        instance.shape = 'some shape'
        instance.state = 'RUNNING'
        instance.time_created = datetime.date(1999, 12, 31)

        return instance

if __name__ == '__main__':
    unittest.main()