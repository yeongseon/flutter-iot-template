import 'package:flutter/material.dart';
import '../models/item.dart';
import '../services/api_service.dart';
import 'edit_item_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  late Future<List<Item>> items;

  @override
  void initState() {
    super.initState();
    items = ApiService.fetchItems();
  }

  void refresh() {
    setState(() {
      items = ApiService.fetchItems();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Item CRUD')),
      body: FutureBuilder<List<Item>>(
        future: items,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            final data = snapshot.data!;
            return ListView.builder(
              itemCount: data.length,
              itemBuilder: (_, i) {
                final item = data[i];
                return ListTile(
                  title: Text(item.name),
                  subtitle: Text(item.description),
                  trailing: IconButton(
                    icon: const Icon(Icons.delete),
                    onPressed: () async {
                      await ApiService.deleteItem(item.id!);
                      refresh();
                    },
                  ),
                  onTap: () async {
                    final result = await Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (_) => EditItemScreen(item: item),
                      ),
                    );
                    if (result != null) refresh();
                  },
                );
              },
            );
          } else if (snapshot.hasError) {
            return Center(child: Text('오류: ${snapshot.error}'));
          }
          return const Center(child: CircularProgressIndicator());
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async {
          final result = await Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => const EditItemScreen()),
          );
          if (result != null) refresh();
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
