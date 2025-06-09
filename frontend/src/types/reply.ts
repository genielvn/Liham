export interface ReplyData {
    id: number;
    body: string;
    created_at: string;
    img_upload: string | null;
    author: string;
    thread_title: string;
    board: string;
    thread: number;
}
