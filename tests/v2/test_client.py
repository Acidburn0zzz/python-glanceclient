# Copyright 2013 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from mox3 import mox
import testtools

from glanceclient.v2 import client


class ClientTest(testtools.TestCase):

    def setUp(self):
        super(ClientTest, self).setUp()
        self.mock = mox.Mox()
        self.mock.StubOutWithMock(client.Client, '_get_image_model')
        self.mock.StubOutWithMock(client.Client, '_get_member_model')

    def tearDown(self):
        super(ClientTest, self).tearDown()
        self.mock.UnsetStubs()

    def test_endpoint(self):
        gc = client.Client("http://example.com")
        self.assertEqual(gc.http_client.endpoint, "http://example.com")

    def test_versioned_endpoint(self):
        gc = client.Client("http://example.com/v2")
        self.assertEqual(gc.http_client.endpoint, "http://example.com")

    def test_versioned_endpoint_with_minor_revision(self):
        gc = client.Client("http://example.com/v2.1")
        self.assertEqual(gc.http_client.endpoint, "http://example.com")
