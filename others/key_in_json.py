# Given a valid json payload, find the first ocurrency of a given a key at any level.
# The payload is recieved as a stream of bytes which means that we can only access
# one character at any given time.

# Assumptions:
# - '"' and ','' are not part of any string keys and values
# - the stream of json is valid we dont need to validate
import json

def next_not_empty_char(stream):
	while stream.has_next():
		char = stream.next()
		if char != ' ':
			return char
	return None

def find_key(key, stream):
	processing_token = False
	token = ''
	# processing string tokens as we see them
	while stream.has_next():
		char = stream.next()
		if char != ' ':
			if char == '"':
				if processing_token:
					# Finish processing current token
					# possible next chars: ':', ',', '}', ']'
					# if next char is ':' it means that found token is a key
					char = next_not_empty_char(stream)
					if char == ':' and key == token:
						# desired token found, the stream points to the beginning of the value
						return
					# found token is not the desired one
					processing_token = False
					token = ""
				else:
					# start processing a new string token
					processing_token = True
			else:
				# Construct the current key as we see it
				if processing_token:
					token += char
	return

def find_value(stream):
	# find the first not empty char of the value whicj is important
	# to understand where the current value finishes given its type
	first_char = stream.next()
	while first_char == " ":
		first_char = stream.next()
	value = first_char
	counts = {'{': 0, '[': 0}
	if first_char in counts:
		counts[first_char] = 1

	# Iterate over the value until we proceess it all 
	while stream.has_next():
		char = stream.next()
		# Finished processing string value
		# as we assumed that " is not a char in any value
		if first_char == '"' and char == '"':
			return value + char
		elif first_char in ['{', '['] and char in ['}', ']']:
			mapping = {'}': '{', ']': '['}
			counts[mapping[char]]-=1
			if counts[first_char] == 0:
				return value + char
		# Finish processing dictonary/array values (similar to parenthesis problem).
		# comma is needed for decimal/integer/boolean values
		elif char in  [',', '}', ']'] and (counts['{'] + counts['[']) == 0:
			return value
		if char in ['{', '[']:
			counts[char]+=1
		value +=char
	return None


def key_in_json(searched_key, stream):
	find_key(searched_key, stream)
	if not stream.has_next():
		return None
	return find_value(stream)


class JsonStream:
	def __init__(self, payload):
		self.payload = payload
		self.pointer = -1

	def next(self):
		self.pointer += 1
		if self.pointer >= len(self.payload):
			raise Exception('End of stream')
		return self.payload[self.pointer]

	def has_next(self):
		return self.pointer < (len(self.payload) -1)

# Test json example:
# {
# 	"integer": 123,
# 	"hash": { "inner_key": {"another_value": "1234"}},
# 	"boolean": true,
# 	"array": [{"value": 1}, {"value": 2}],
# 	"decimal": 12.234
# }

payload = "{\"integer\":123,\"hash\":{\"inner_key\":{\"another_key\": \"1234\"}},\"boolean\":true,\"array\":[{\"value\":1},{\"value\":2}],\"decimal\":12.234}"
print('json_payload:', json.loads(payload))

for key in ['integer', 'hash', 'inner_key', 'another_key', 'boolean', 'array', 'value', 'decimal', 'unexisting_key']:
	stream = JsonStream(payload)
	print('key: ',  key, ' found_value: ', key_in_json(key, stream))