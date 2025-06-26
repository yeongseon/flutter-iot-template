import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/item.dart';

class ApiService {
  // ✅ Use localhost for Flutter Web; replace with your actual IP if needed
  static const String baseUrl = 'http://localhost:8000/api/v1';

  static Future<List<Item>> fetchItems() async {
    final response = await http.get(Uri.parse('$baseUrl/items'));
    if (response.statusCode == 200) {
      return (json.decode(response.body) as List)
          .map((json) => Item.fromJson(json))
          .toList();
    } else {
      throw Exception('Failed to load items');
    }
  }

  static Future<Item> createItem(Item item) async {
    final response = await http.post(
      Uri.parse('$baseUrl/items'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(item.toJson()),
    );
    if (response.statusCode == 200 || response.statusCode == 201) {
      return Item.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to create item');
    }
  }

  static Future<Item> updateItem(Item item) async {
    final response = await http.put(
      Uri.parse('$baseUrl/items/${item.id}'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode(item.toJson()),
    );
    if (response.statusCode == 200) {
      return Item.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to update item');
    }
  }

  static Future<void> deleteItem(int id) async {
    final response = await http.delete(Uri.parse('$baseUrl/items/$id'));
    if (response.statusCode != 200) {
      throw Exception('Failed to delete item');
    }
  }
}
