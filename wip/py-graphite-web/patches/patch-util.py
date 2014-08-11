$NetBSD$

include graphite.intervals and collections.deque so that carbonlink
works
--- webapp/graphite/util.py	2014-08-11 11:56:11.627654856 +0100
+++ webapp/graphite/util.py	2014-08-11 12:03:01.323663825 +0100
@@ -12,6 +12,8 @@
 See the License for the specific language governing permissions and
 limitations under the License."""
 
+import sys
+
 try:
   import cPickle as pickle
   USING_CPICKLE = True
@@ -89,6 +91,8 @@
     PICKLE_SAFE = {
       'copy_reg': set(['_reconstructor']),
       '__builtin__': set(['object']),
+      'graphite.intervals': set(['Interval', 'IntervalSet']),
+      'collections': set(['deque']),
     }
 
     @classmethod
@@ -112,6 +116,8 @@
     PICKLE_SAFE = {
       'copy_reg': set(['_reconstructor']),
       '__builtin__': set(['object']),
+      'graphite.intervals': set(['Interval', 'IntervalSet']),
+      'collections': set(['deque']),
     }
 
     def find_class(self, module, name):

