import os
import unittest
import ssh

key1 = "ssh-rsa AAAA"
key2 = "ssh-rsa BBBB"
key3 = "ssh-rsa CCCC"

class TestSSH(unittest.TestCase):
    def tearDown(self):
        """Delete mockup file"""
        pass

    def test_makeAuthorizedKey(self):
        """docstring"""
        theKey = 'command="gitube-serve harry",no-port-forwarding,no-X11-forwarding,no-agent-forwarding,no-pty ' + key1
        self.assertEqual(theKey, ssh.makeAuthorizedKey('harry', key1))

    def test_write_key(self):
        tmp = self.getTmp()
        ssh.writeKey(tmp, 'harry', key1)
        ssh.writeKey(tmp, 'harry', key2)
        ssh.writeKey(tmp, 'harry', key3)

        f = open(tmp, 'r')
        self.assertEqual(ssh.makeAuthorizedKey('harry', key1)+'\n', f.readline())
        self.assertEqual(ssh.makeAuthorizedKey('harry', key2)+'\n', f.readline())
        self.assertEqual(ssh.makeAuthorizedKey('harry', key3)+'\n', f.readline())

        f.close()
        os.remove(tmp)

    def test_remove_key(self):
        tmp = self.getTmp()
        ssh.writeKey(tmp, 'harry', key1)
        ssh.writeKey(tmp, 'harry', key2)
        ssh.writeKey(tmp, 'harry', key3)
        
        k1 = ssh.makeAuthorizedKey('harry', key1) + '\n'
        k2 = ssh.makeAuthorizedKey('harry', key2) + '\n'
        k3 = ssh.makeAuthorizedKey('harry', key3) + '\n'

        f = open(tmp, 'r')
        self.assertEqual(f.readlines(), [k1, k2, k3])
        f.close()

        ssh.removeKey(tmp, 'harry', key2)
        f = open(tmp, 'r')
        self.assertEqual(f.readlines(), [k1, k3])
        f.close()

        os.remove(tmp)

    def getTmp(self):
        return '/tmp/gitube_test_%d.tmp' % os.getpid()

def main():
    unittest.main()

if __name__ == '__main__':
    main()
