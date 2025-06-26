import 'package:flutter/material.dart';
import '../models/item.dart';
import '../services/api_service.dart';

class EditItemScreen extends StatefulWidget {
  final Item? item;
  const EditItemScreen({super.key, this.item});

  @override
  State<EditItemScreen> createState() => _EditItemScreenState();
}

class _EditItemScreenState extends State<EditItemScreen> {
  final _formKey = GlobalKey<FormState>();
  late String name;
  late String description;

  @override
  void initState() {
    super.initState();
    name = widget.item?.name ?? '';
    description = widget.item?.description ?? '';
  }

  void _submit() async {
    if (!_formKey.currentState!.validate()) return;
    _formKey.currentState!.save();
    final newItem = Item(id: widget.item?.id, name: name, description: description);
    try {
      final result = widget.item == null
          ? await ApiService.createItem(newItem)
          : await ApiService.updateItem(newItem);
      Navigator.pop(context, result);
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('저장 실패: $e')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.item == null ? '아이템 추가' : '아이템 수정'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Form(
          key: _formKey,
          child: Column(children: [
            TextFormField(
              initialValue: name,
              decoration: const InputDecoration(labelText: '이름'),
              validator: (v) => v!.isEmpty ? '이름을 입력하세요' : null,
              onSaved: (v) => name = v!,
            ),
            TextFormField(
              initialValue: description,
              decoration: const InputDecoration(labelText: '설명'),
              validator: (v) => v!.isEmpty ? '설명을 입력하세요' : null,
              onSaved: (v) => description = v!,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _submit,
              child: const Text('저장'),
            )
          ]),
        ),
      ),
    );
  }
}
