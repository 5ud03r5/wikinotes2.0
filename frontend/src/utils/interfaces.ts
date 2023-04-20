export interface Article {
  title: string;
  text: string;
  tags?: Tag[];
  id: string;
}

export interface Tag {
  name: string;
  id: string;
}

export interface Note {
  text: string;
  id: string;
}
