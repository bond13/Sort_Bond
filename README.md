Sort_Bond

Brandon Bond
0920205
Instafeed
=========

Url sort individual exercise

The implemented validator that was designed from excercise 3 (listed breifly
below) and explained fully in prev_README.md. The implementation to validate
and compare URLs is done in url.py. The normalizer is done using 
url_normalize.py, which was written by Nikolia Panov. Much of the url.py
was also already implemented from previous weeks.

I added the validator functionality to  main.py which is to be run
using the command:
  python main.py [--valid|--invalid] input-file output-file

The input file still much have 1 url per line (same as previous assignment)
and 1 url will be printed per line in the output file (same as before). 

If the valid flag is set, only the valid URLs will be sorted and printed
in the given output file. This is the same if the invalid flag is set, only 
the invalid URLs will be sorted and printed in the output file. For both
valid and invalid, the URLs will be sorted on their canonicalized form. The 
sort algorithms use the standard string operators <, >, and == on the 
canonicalized form. If neither flag is set, the valid URLs will be sorted
and printed to the output file followed by the invalid URLs sorted and printed
after the valid ones. The implementation in main simply separates the 
valid and invalid URLs first before sorting/printingg them in the end, so they
were sorted separately. I thought this created less checks and simplified
the python by manually doing the first part of the sort and using python
for the string comparisons. With my limited python skills, this was quicker
and worked better for this particular assignment, but full comparators
are implemented for our URL objects (which was done earlier by Chee Wei).

The  main program automically prints all the URLs in read-order to standard out.
This included the source url, whether it is valid, its canonicalized form,
whether its source url is unique and whether its canonicalized url is unique.
The functionality of the sort and read-order printing was combined into the main
to simply to implementation and use of the program. The user now only has to run
one python script and will be able to access both the sorted list and printed
out information all from one input file. This was done to make the client be
able to get al the output they need with 1 call instead of 2 completely separate
but very similar programs. Implementation was simplified as well since we
were already reading in the file and create URL objects for each. The only 
drawback is an output file still needs to be listed even if the user only
wants to see the in order printing. This is very simple for the user to do,
but they will get an unwanted file which I thought more convenient for the user
than 2 different programs being run.

Unit tests for the validator, canonicalizer and comparators are written in 
validatorTests.py. This set of python unit tests runs test cases to ensure
valid URLs are correctly identified as valid. It then goes through and tests
our list of rules for invalid urls to ensure invalid URLs are properly
identified as well. This same approach was taken for the canonicalizer tests
since our definitions of valid and normal are strongly coupled. I tested
both URLs already in their canonical form as wel as each of the various rules
our canonicalizer addresses to see if that is done correctly. Since the
comparators are simply the string comparitors I used the default less, greater,
and equal functions on various canonicalized URLs just like my program does.
I tested almost all of the important cases our canonicalizer addresses to
ensure main.py is outputing the correct information.

URL Validator/Canonicalizer Rules:

A URL in canonical form follows these rules:
<ul>
  <li>Take care of IDN domains.
  <li>Convert the scheme and host to lower case.</li>
  <li>Capitalize letters in escape sequences.</li>
  <li>Decode percent-encoded octets of unreserved characters.</li>
  <li>Remove the default port.</li>
  <li>Remove dot-segments.</li>
  <li>Remove duplicate slashes.</li>
  <li>Remove the "?" when the query is empty.</li>
  <li>Use 'http' schema by default when appropriate.</li>
  <li>For schemes that define a default authority, use an empty authority if the default is desired.</li>
  <li>For schemes that define an empty path to be equivalent to a path of "/", use "/".</li>
  <li>All portions of the URI must be utf-8 encoded NFC from Unicode strings.</li>
</ul>

A URL is considered valid if the source URL matches its canonicalized form.
URLs are compared based on string operators on their canonicalized form.