import style from "./Board.module.scss";
import Link from "next/link";

interface BoardProps {
    id: string; 
    name: string;
    description: string;
}

const Board: React.FC<BoardProps> = ({ id, name, description }) => {
    return (
        <Link href={`b/${id}`} style={{ textDecoration: "none" }}>
            <div className={style.board}>
                <div className={style.board__name}>{name}</div>
                <div className={style.board__description}>{description}</div>
            </div>
        </Link>
    );
};

export default Board;
