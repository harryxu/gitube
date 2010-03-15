import unittest
import ssh

key1 = "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAnNt3hQjf1KApe7qPhg7lE2+HOS8VO/nqteTd83BGY86+2lQhXyVN4bzwN0baRc+A/OZMKbnZ9amIdaoOsusOJGEpcx0hIr4XsVAvO/iOu+byPTtoxSxDP4GBj9N50BN+mMgjsf63jjrynL9Q3gIk+t9MY7lxB0+hVQlQvE0LRMtRw0vp21Fe4nGxN0zg4YlKBVqSYpORrGbh3T/UBHRxYikTEm2mPbVzwBAo+3Tl/129Vlv/6eRFcfrmHPc1wK1+l95H/ct+hCRkyhBjRLWVQ24RTjebvS1ndUBh5e4YoN7S7POPhyvKdCx2I9/hx9CSyF1EW8Hsghpl3Pka8TOovw== harry@harry-laptop"

class TestSSH(unittest.TestCase):
    def tearDown(self):
        """Delete mockup file"""
        pass

    def test_makeAuthorizedKey(self):
        """docstring"""
        theKey = 'command="gitube-serve harry",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ' + key1
        self.assertEqual(theKey, ssh.makeAuthorizedKey('harry', key1))

    def test_write_key(self):
        ssh.writeKey('/tmp/asss', 'harry', key1)

    def test_remove_key(self):
        self.fail('not implement')

def main():
    unittest.main()

if __name__ == '__main__':
    main()
