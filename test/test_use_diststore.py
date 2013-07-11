
import os
import tempfile
import shutil

from tiddlywebplugins.bfw import init

from tiddlyweb.model.bag import Bag
from tiddlyweb.config import config

from tiddlywebplugins.utils import get_store

def setup_module(module):
    module.TMPDIR = tempfile.mkdtemp()

    config['server_store'] = ['text', {
        'store_root': os.path.join(TMPDIR, 'store')
    }]
    
    init(config)

    module.store = get_store(config)


def teardown_module(module):
    shutil.rmtree(TMPDIR)

def test_default_bags():
    bags = store.list_bags()
    assert len(bags) == 1
    assert bags[0].name == 'assets'

def test_create_bag():
    bag_name = 'a bag'
    store.put(Bag(bag_name))
    
    bag = store.get(Bag(bag_name))

    assert bag.name == bag_name

    bags = store.list_bags()
    assert len(bags) == 2

    assert sorted([bag.name for bag in bags]) == [bag_name, 'assets']
