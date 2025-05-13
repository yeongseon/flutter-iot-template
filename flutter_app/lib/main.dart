import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flutter + FastAPI',
      home: HelloScreen(),
    );
  }
}

class HelloScreen extends StatefulWidget {
  const HelloScreen({super.key});
  @override
  State<HelloScreen> createState() => _HelloScreenState();
}

class _HelloScreenState extends State<HelloScreen> {
  String _message = 'Loading...';

  @override
  void initState() {
    super.initState();
    _fetchHelloMessage();
  }

  Future<void> _fetchHelloMessage() async {
    try {
      final response = await http.get(Uri.parse('http://10.0.2.2:8000/hello')); // Android 에뮬레이터에서는 localhost 대신 10.0.2.2
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        setState(() {
          _message = data['message'] ?? 'No message';
        });
      } else {
        setState(() {
          _message = 'Failed with status ${response.statusCode}';
        });
      }
    } catch (e) {
      setState(() {
        _message = 'Error: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('API Test')),
      body: Center(child: Text(_message, style: const TextStyle(fontSize: 20))),
    );
  }
}
