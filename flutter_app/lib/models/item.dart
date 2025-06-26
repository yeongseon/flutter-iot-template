class Item {
  final int? id;
  final String name;
  final String description;

  Item({this.id, required this.name, required this.description});

  factory Item.fromJson(Map<String, dynamic> json) => Item(
        id: json['id'],
        name: json['name'],
        description: json['description'],
      );

  Map<String, dynamic> toJson() => {
        'name': name,
        'description': description,
      };
}
